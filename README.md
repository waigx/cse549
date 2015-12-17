# CSE549

This is README file for Course Project CSE-549

* Topic: UI for RNA-seq quantification
* Professor: Rob Patro
* Due Date: Dec 16, 2015
* Students:

|Name          |   SBU ID      |        Email               |          Git ID            |
|--------------|:-------------:|:--------------------------:|:--------------------------:|
| Jian Yang    |  110168771    | yang16@cs.stonybrook.edu   |       SwordYoung           |
| Hongjin Zhu  |  109748818    | hozzhu@cs.stonybrook.edu   |  Alviss-zhj, Hongjin Zhu   |
| Jianglin Wu  |  108075432    | jiangwu@cs.stonybrook.edu  | jianglin101, Jianglin Wu   |
| Yigong Wang  |  109973706    | yigwang@cs.stonybrook.edu  |          waigx             |

### Directories and Files
In this submitted project, there are several directories and files included:
 - report: the report directory
 - server: the code for the project
 - CSE549_demo.mov: video demo of the project

### Run server:
go to directory where manage.py locates (./server/) and run:
$ python manage.py runserver 8000

Resource:

### Useful websites

* Sample demo
	Sample demo is included in the main path named CSE549_demo.mov
	A clear version for the sample demo can be seen at:
	- https://drive.google.com/file/d/0B7S08uGtvwqkcl91ekZ6U1dES0E/view?usp=sharing
	- https://www.dropbox.com/s/gp7i7kngr7uneer/CSE549-demo.mov?dl=0

* Sample project:

        http://lair.berkeley.edu/ellahi/
        https://github.com/pachterlab/sleuth
        
        http://fantom.gsc.riken.jp/zenbu/gLyphs/#config=64Bm-JzKJdjrAhl2rKyj_B

* Bootstrap Library (CSS):



        http://getbootstrap.com

* Data Visualization Library (JavaScript):



        http://d3js.org
        https://github.com/mbostock/d3
        http://www.chartjs.org


### Requirements:

High throughput RNA-seq data contain millions of reads which are aligned/mapped to the reference transcriptome with a mapper.  Subsequently, a tool is used to report the expression level of different transcripts in the experimental sample corresponding to the reads. The output from the quantifier (such as RSEM) typically consists of many numerical results, and little visual aid to help interpret these results. In this project we aim to make a rich, interactive, web interface, which serves a data-exploration tool for the end-user (usually a Biologist or Bioinformatician).  The visualizations here should be interactive, implemented, most likely, using a javascript framework.

Given the appropriate input (a set of abundance estimates — one of which may be the “ground-truth”) the framework should:
 1. Generate plots and tables to explore different quality metrics (e.g.number of reads mapped in the experiment, transcript GC content versus abundance estimates, transcript length versus abundance estimates, and other possible confounding factors versus abundance estimates).
 2. Create interactive plots, in the sense that a user should be able to access a data point (which is a transcript here) and by clicking on it, obtain abundance measure across all the methods / experiments etc.  If the provided quantification estimates have samples or variances associated with the abundance, the user should be able to plot and explore these interactively as well by selecting a transcript or set of transcripts.
 3. If the user specifies that one of the provided abundance results is the “truth” (e.g. in a simulated dataset), the framework should compute a collection of different accuracy metrics and compare all other estimates according to these.  Some such metrics are pearson correlation, spearman correlation, proportionality correlation, mean absolute error, true positive fraction and false positive rate.  These should be provided in the form of a nicely formatted table where appropriate, and if a specific result is chosen, plots (e.g. scatter plots) should be generated on demand.
 4. Remaining credit will be granted for useful and interesting visualizations and metrics that you come up with.

The goal here is really to provide an interactive, aesthetically pleasing, and useful tool for the interactive exploration of RNA-seq abundance estimation results.
