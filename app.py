"""Estimate technical batch offsets while retaining a fictional biological condition effect."""
from kit import *
TITLE='Condition-Preserving Metabolomics Batch Correction'
LIVE=False

def design(condition,batch,batches=4):return np.column_stack([np.ones(len(batch)),condition,np.eye(batches)[batch][:,1:]])
def fit(values,condition,batch):
    z=design(condition,batch);return np.linalg.lstsq(z,values,rcond=None)[0]
def correct(values,batch,weights):return values-np.eye(4)[batch][:,1:]@weights[2:]
def run(d,a):
    rng=np.random.default_rng(a.seed);n=800;batch=rng.integers(0,4,n);condition=rng.integers(0,2,n);base=rng.normal(size=(n,18))*.2;signal=np.linspace(.3,1.3,18);clean=base+condition[:,None]*signal;offsets=rng.normal(0,1.2,(4,18));offsets[0]=0;observed=clean+offsets[batch];tr=np.arange(600);te=np.arange(600,800);w=fit(observed[tr],condition[tr],batch[tr]);corrected=correct(observed[te],batch[te],w)
    batch_means=np.array([observed[tr][batch[tr]==b].mean(axis=0) for b in range(4)]);naive=observed[te]-(batch_means[batch[te]]-batch_means[0])
    return dict(raw_to_clean_rmse=rmse(clean[te],observed[te]),corrected_to_clean_rmse=rmse(clean[te],corrected),naive_centering_to_clean_rmse=rmse(clean[te],naive),training_samples=600,test_samples=200,test_batch_labels_known=True,test_condition_labels_used_for_correction=False,scope='Known-batch synthetic correction; no disease interpretation'),dict(batch_coefficients=w,observed=observed[te],corrected=corrected,hidden_clean=clean[te])

if __name__=="__main__":main(run)
