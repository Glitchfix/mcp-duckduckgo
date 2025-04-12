# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Install uv
RUN pip install uv

# Copy the project definition file
COPY pyproject.toml .

# Install dependencies using uv
RUN uv sync

# Copy the rest of the application code
COPY . .

# Make the script executable
RUN chmod +x app.py

# Run the FastMCP server with stdio transport
CMD ["python", "app.py"]
