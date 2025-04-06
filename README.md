# Code Repository for IR Research Project as part of TU Delft DSAIT4050 - Group 33

## How to recreate results

1. Upload file [Noise_Types_Per_Batch.ipynb](Noise_Types_Per_Batch.ipynb) to Kaggle
2. Run with GPU enabled
3. Expect a run-time of about 1.5 hrs.

## Files:

- [Noise_Types_Per_Batch.ipynb](Noise_Types_Per_Batch.ipynb) - 
**Contains all the graphs from our paper.** Compares the performance on of different noise levels and types and
different batches of Character Error Rate (CER) vs Word Error Rate (WER). All other files were helpful for us
to derive the results in this one.

- [Colbert_Final_evaluation.ipynb](Colbert_Final_evaluation.ipynb) - 
Runs experiments similiar to [Noise_Types_Per_Batch.ipynb](Noise_Types_Per_Batch.ipynb) but with only some
subgraphs created.

- [Document_noise.ipynb](Document_noise.ipynb) - 
An attempt to assess the feasibility of adding noise to documents and not only queries

- [model_comparison.ipynb](model_comparison.ipynb) -
Compares the performance of various simple Pyterrier retrievers

- [noise_types.ipynb](noise_types.ipynb) - 
A much more detailed analysis of noise types, some of which not included in the final experiment

- [original_example.ipynb](original_example.ipynb) - A sample starting file on how to use frameworks