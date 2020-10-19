 - [Company Name Matching](https://github.com/kuanmin/projects/tree/master/Company%20Name%20Matching) (`Python`) <br />
   - Some input data are built by handwriting and scanning afterwards or by typing, which might cause data inconsistency and wrong inputs. This will lead to tremendous problems for end users, such as product managers and analysts. We want to avoid any operational inefficiency involving manual correction or misleading statistics or analysis at the further end of the reporting process. Regarding company names, besides typo, different name suffix, such GmbH or Ltd, may cause issue of distinguishability. 
   - This is my attempt applying different type of **Identity Resolution** approaches, such as **jaccard**, **jaro winkler**, **hamming**, **levenshtein**, and **ratcliff obershelp**, to analyse the company name dataset. we also apply **Block methods** with criteria *country* to avoid unnecessary comparisons and reduce quadratic runtime complexity. The goal is to choose an approach to 1.)have the most similar with the similarity up to a threshold, and 2.)make sure the most similar has a certain level of difference between itself and the second most similar, so to perform precise classification.
<p align="center">
  <img width="80%" height="90%" src="https://github.com/kuanmin/projects/blob/master/Company%20Name%20Matching/output_example.png">
</p>
<p align="center">
  <img width="65%" height="80%" src="https://github.com/kuanmin/projects/blob/master/Company%20Name%20Matching/analysis.png">
</p>
