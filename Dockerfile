# Use the base image with Python 3.10 and Node.js 19
FROM nikolaik/python-nodejs:python3.10-nodejs19

# Update sources to use Debian archive and disable expired repo checks
RUN sed -i 's|http://deb.debian.org/debian|http://archive.debian.org/debian|g' /etc/apt/sources.list && \
    sed -i 's|http://security.debian.org|http://archive.debian.org|g' /etc/apt/sources.list && \
    echo 'Acquire::Check-Valid-Until "false";' > /etc/apt/apt.conf.d/99no-check-valid-until && \
    apt-get update && \
    apt-get install -y --no-install-recommends ffmpeg && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Copy application code
COPY . /app/

# Set the working directory
WORKDIR /app/

# Upgrade pip and setuptools
RUN python3 -m pip install --upgrade pip setuptools

# Install Python dependencies
RUN pip3 install --no-cache-dir --upgrade --requirement requirements.txt

# Default command to run when container starts
CMD ["bash", "start"]
``
