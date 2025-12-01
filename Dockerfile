# Create a base image
FROM python:3.8-slim

# set wrkdir
WORKDIR /app/

# Copy files
COPY . .

# install dependieces
RUN pip install --no-cache -r requirements.txt

# COPY Diff structues
# COPY ./models/ ./models/
# COPY ./Dataset/ ./Dataset/
# COPY ./templates/ ./templates/
# COPY ./static/ ./static/  

# Expose port
EXPOSE 5000

# Run final command statement
CMD ["python" , "app.py"]
