- types of recommender system :
- popularity based : based on formula 
- content based : based on similarty
- collobaratoy filtering: 
- hybrid : mixture of all of the following

1) Copy files
COPY . .

2) install dependieces
RUN pip install --no-cache -r requirements.txt,

if we make changes in app file. step 1 will be chached invalidate, hence step 2 will be need to rebuild.
- In docker file, write command that doesn't changes with version first so that they won;t get cached invalidated.
