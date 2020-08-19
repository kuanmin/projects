Projects:<br />
(Click on the project name for reports, presentations, and analyses.)

 - [Enhancement of LibKGE](https://github.com/kuanmin/kge-work) (`Python`) (Ongoing project / my thesis work.)<br />
    - Open source LibKGE framework is a PyTorch-based library for efficient training, evaluation, and hyperparameter optimization of [knowledge graph embeddings](https://ieeexplore.ieee.org/document/8047276) (KGE). The key goal is to foster reproducible research into (as well as meaningful comparisons between) KGE models and training methods. As the authors argue in [ICLR 2020 paper](https://openreview.net/forum?id=BkxSmlBFvr), the choice of training strategy and hyperparameters are very influential on model performance, often more so than the model class itself.
    - I implement new functions to LibKGE, which will allow the New package to run training and validation, not just on single KGE model, but *multiple models* in one process, so to be able to performe **joint training** and **alternative training models**.
    
 - [Profitability - Statistical Analysis with Excel VBA](https://github.com/kuanmin/projects/tree/master/Profitability%20Analysis%20with%20Excel%20VBA) (`VBA`) <br />
   - Our team of actuaries play a vital role in our organization. Our daily works relate to actuarial analysis, including **Modelling**, **Predicting**, **Profit and Surplus Analysis**, **Risk and Uncertainty**, and **Validation**. And Excel has been applied to parts of these tasks along with the use of VBA. Here are some examples from my work.
   - Click on the images to see the originals. From left to right, up to down: *asset sheet* - *assumption* - *profit analysis* - *sensitivity test*
<p align="center">
  <img width="42%" height="42%" src="https://github.com/kuanmin/projects/blob/master/Profitability%20Analysis%20with%20Excel%20VBA/asset_sheet.png">
  <img width="42%" height="42%" src="https://github.com/kuanmin/projects/blob/master/Profitability%20Analysis%20with%20Excel%20VBA/assumption.png">
</p>

<p align="center">
  <img width="42%" height="42%" src="https://github.com/kuanmin/projects/blob/master/Profitability%20Analysis%20with%20Excel%20VBA/profit_analysis.png">
  <img width="42%" height="42%" src="https://github.com/kuanmin/projects/blob/master/Profitability%20Analysis%20with%20Excel%20VBA/sensitivity_test.png">
</p>
<p align="center">
  <img width="80%" height="80%" src="https://github.com/kuanmin/projects/blob/master/Profitability%20Analysis%20with%20Excel%20VBA/VBA.png">
</p>

 - [Information Retrieval on NLTK corpora](https://github.com/kuanmin/projects/tree/master/Information%20Retrieval) (`Python`) <br />
   - In this project, we discuss the implementation of a **Latent Semantic Indexing**-based information retrieval model, and evaluates its performance against the **Vector Space Model** on a collection with 18,828 documents.
   
 - [Data Infrastructure](https://github.com/kuanmin/projects/blob/master/Data%20Infrastructure/data_pipeline.png) (`SQL` / *PostgreSQL*) <br />
   - While working in the data team of Risk Management department, we deal with financial products and the transactions. Our work is to maintain and improve the data infrastructure of the settlement process. This involves **data pipeline**, **data checks**, **data modeling**, and **data warehouse**. Here are the examples for *data pipeline* and *data model* from our work.
<p align="center">
  <img width="70%" height="80%" src="https://github.com/kuanmin/projects/blob/master/Data%20Infrastructure/data_pipeline.png">
</p>
<p align="center">
  <img width="70%" height="80%" src="https://github.com/kuanmin/projects/blob/master/Data%20Infrastructure/Data_Model.png">
</p>



 - [Automated ICD Coding](https://github.com/kuanmin/projects/tree/master/ICD%20matching) (`Python`) <br />
   - To reduce coding errors and cost, this is my attempt applying **Latent Semantic Indexing** to build an ICD coding machine which automatically and accurately translates
the free-text diagnosis descriptions into ICD codes.
<p align="center">
  <img width="80%" height="80%" src="https://github.com/kuanmin/projects/blob/master/ICD%20matching/output_example.png">
</p>

 - [Company Name Matching](https://github.com/kuanmin/projects/tree/master/Company%20Name%20Matching) (`Python`) <br />
   - Some input data are built by handwriting and scanning afterwards or by typing, which might cause data inconsistency and wrong inputs. This will lead to tremendous problems for end users, such as product managers and analysts. We want to avoid any operational inefficiency involving manual correction or misleading statistics or analysis at the further end of the reporting process. Regarding company names, besides typo, different name suffix, such GmbH or Ltd, may cause issue of distinguishability. 
   - This is my attempt applying different type of **Identity Resolution** approaches, such as **jaccard**, **jaro winkler**, **hamming**, **levenshtein**, and **ratcliff obershelp**, to analyse the company name dataset. we also apply **Block methods** with criteria *country* to avoid unnecessary comparisons and reduce quadratic runtime complexity. The goal is to choose an approach to 1.)have the most similar with the similarity up to a threshold, and 2.)make sure the most similar has a certain level of difference between itself and the second most similar, so to perform precise classification.
<p align="center">
  <img width="80%" height="90%" src="https://github.com/kuanmin/projects/blob/master/Company%20Name%20Matching/output_example.png">
</p>
<p align="center">
  <img width="65%" height="80%" src="https://github.com/kuanmin/projects/blob/master/Company%20Name%20Matching/analysis.png">
</p>

 - [Recipe Finder](https://github.com/kuanmin/projects/tree/master/Recipe%20Finder) (`Java`, `RDFS`, `SPARQL`, `SQL`, `JavaScript` / *Apache Jena*) <br />
   - Apache Jena, a Java framework, is a well-known Semantic Web programming framework. In this project, data knowledge related to **Linked Open Data** and **Ontology engineering** are applied. 
   - We build an API using Apache Jena providing households with an easy way to find recipes incorporating food they need to either consume today or throw away tomorrow. We tapped into the power of the Semantic Web and developed an application which allows its users to browse recipes based on leftovers they might have in their kitchen, ultimately reducing food waste. 
<p align="center">
  <img width="80%" height="80%" src="https://github.com/kuanmin/projects/blob/master/Recipe%20Finder/pics/combined.PNG">
</p>

 - [Data & Matrix](https://github.com/kuanmin/projects/tree/master/Data%20and%20Matrix) (`R`) <br />
   - In these tasks, data analytical skills related to **Matrix Completion**, **Non-Negative Matrix Factorization**, and **Singular Value Decomposition** are applied.
<p align="center">
  <img width="50%" height="50%" src="https://github.com/kuanmin/projects/blob/master/Data%20and%20Matrix/pics/recovered.png">
</p>

 - [Integrating Web Data on Video Games and Companies](https://github.com/kuanmin/projects/tree/master/Integrating%20Web%20Data) (`Python`, `Java`, `XML` / *MapForce*) <br />
   - In this project, we worked with Python and Java libraries BeautifulSoup, Selenium WebDriver, and Jsoup3. And data analytical skills related to **Data Translation**, **Identity Resolution**, and **Data Fusion** are applied.
   - We focus on building an integrated database of video games and video game developers which will be informative to video game players and professionals working in the industry alike. Our combined data can offer interesting new visions that can assist on business decision making and drive video game businesses to a success. Simply by exploring and mining this data, one will be able to gain a better understanding of current video game trends. 
   - For example, our integrated data can provide answers on manifold questions such as ‘Which game platform currently generates the most revenue?’, ‘Which genre types are most popular among the users?’, ’How does game experts’ judgment affect the market sales‘, or ‘How does the revenue of games differ from the worldwide regions?’.
<p align="center">
  <img width="50%" height="50%" src="https://github.com/kuanmin/projects/blob/master/Integrating%20Web%20Data/VideoGames_Shema.png"/>
  <img width="31%" height="31%" src="https://github.com/kuanmin/projects/blob/master/Integrating%20Web%20Data/VideoGames_Shema_2.png"/>
</p>
   
 - [AI-Based Insurance Broker](https://github.com/kuanmin/projects/tree/master/AI-Based%20Insurance%20Broker) (`Java`, `JSON`, `JavaScript`, *Java AWT*, *NetBeans*, *MongoDB*, *React*, *Flask*) <br />
   - In this project, data knowledge related to **Ontology engineering** and **Multiple-criteria decision analysis** are applied. 
   - We want to shed light onto the current technological state of the insurance broker industry and how AI may transform it. Furthermore, we provide an Recommender System for dental insurances using the **Technique for Order of Preference by Similarity to Ideal Solution** (TOPSIS), a popular **Multiple Criteria Decision Making Method** (MCDM). In addition we design an architectural model which may serve as an example of how to implement an insurance recommender system as a web application with state of the art technology.

<p align="center">
  <img width="80%" height="80%" src="https://github.com/kuanmin/projects/blob/master/AI-Based%20Insurance%20Broker/chain.png"/>
</p>
<p align="center">
  <img width="38%" height="38%" src="https://github.com/kuanmin/projects/blob/master/AI-Based%20Insurance%20Broker/React_01.png"/>
  <img width="38%" height="38%" src="https://github.com/kuanmin/projects/blob/master/AI-Based%20Insurance%20Broker/React_02.png"/>
</p>


   
