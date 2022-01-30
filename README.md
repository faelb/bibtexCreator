# bibtexCreator

-> to use this little program: 
1. create your own python environment (to not mess up
your own installation with all the modules)
go into the cloned git folder of the project and run:

python3 -m venv nameOfEnv.venv

this creates the venv\ folder

then use this venv as the python interpreter for execution:
in windows go to the venv folder and run the activate script
 <DIR>\venv\Scripts\activate

now the venv is the active interpreter and you can go to step 2

2. install all the needed dependencies of the program:
go to the main folder of the program where the requirements.txt is located
then execute:

pip install -r requirements.txt

this will install everything that is needed to run the program

3. run the program

with the venv being active now just run:

python3 creator.py 


a small program where you can give your input for Internet articles to convert them into a Bibtex, which in term can be used for your BachelorThesis and the use of a Reference Atomation Software (f.e. Jabref)

it's very basic - don't expect something big

the problem with my first bac thesis was that everytime I had to add a reference to JabRef that was not a sweet Bibtex from ieee website or anywhere (mainly for website cites)
it was quite cumbersome to use the interface of JabRef to add such a new cite.
It's much more convenient to just copy a bibtex and let it add the metadata to jabref automatically.
So with this small programm you just copy paste the url of the article, and it will crawl through the website for the metadata,
afterwards it will show you what it found and if needed you can change it.
Then the bibtex will be copied to your clipboard so you can just paste it with Ctrl+V
 
 
 this means that for example: https://www.smartinsights.com/social-media-marketing/social-media-strategy/new-global-social-media-research/
 is transformed to:
 
 @Article{3TeVoT4=,
  author  = {Annmarie Hanlon and Lilach Bullock},
  journal = {smartinsights.com},
  title   = {Global social media statistics research summary 2022},
  year    = {2022},
  note    = {30.01.2022},
  url     = {https://www.smartinsights.com/social-media-marketing/social-media-strategy/new-global-social-media-research/},
} 


This should help me with my bac2 alot ; )


Short note:  the refIndex which is is created by a hash of the url, so you can just copy and use it and it should in most times be unique
