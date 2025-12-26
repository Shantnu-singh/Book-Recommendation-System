# Create a base image
FROM python:3.8-slim

# set wrkdir
WORKDIR /app/

# Copy requirements file
COPY requirements.txt/ .

# install dependieces
RUN pip install --no-cache-dir -r requirements.txt

# Copy all files
COPY . . 

# Add env
ENV PORT=5000 

# Expose port
EXPOSE 5000

# Run final command statement
CMD ["python" , "app.py"]
