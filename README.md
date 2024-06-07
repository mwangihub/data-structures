# Data Structures and Algorithms in Python

This project contains various implementations of data structures and algorithms written in Python. Additionally, it includes a Django server that currently displays a simple homepage. Future enhancements will include graphical representations of different algorithms and data structures.

## Project Structure

The project is organized into the following main modules:

### Start Package

1. **gpa.py**:

   - A Python program that computes a grade-point average (GPA). This script allows users to input their grades and calculates the average based on the standard 4.0 GPA scale.

2. **sort.py**:
   - An algorithm that takes user input and sorts the numbers in ascending order. This script demonstrates the implementation of sorting algorithms.

### Algorithms Package

This package contains various algorithmic practices and examples:

- **Gauss**:

  - A script that demonstrates the calculation of the sum of the first `n` natural numbers using Gauss's formula.

- **ValidAnagram**:
  - A function to determine if two strings are anagrams of each other. It checks if one string can be rearranged to form the other.

### Search Package

This package includes advanced search algorithms:

- **maze.py node.py**:

  - An implementation of the breadth-first search (BFS) algorithm. BFS is used for traversing or searching tree or graph data structures. It starts at the tree root (or an arbitrary node of a graph) and explores the neighbor nodes at the present depth prior to moving on to nodes at the next depth level.

  - An implementation of the depth-first search (DFS) algorithm. DFS is used for traversing or searching tree or graph data structures. The algorithm starts at the root node (selecting some arbitrary node as the root node in the case of a graph) and explores as far as possible along each branch before backtracking.

### Server Package

The server package contains a Django server setup that currently displays a simple homepage. In the future, this server will be used to graphically represent different algorithms and data structures, providing a visual aid to understanding how they work.

## Getting Started

To get started with this project, follow these steps:

1. **Clone the repository**:

2. **Set up a virtual environment** (optional but recommended):

   ```sh
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages**:

   ```sh
   pip install -r requirements.txt
   ```

4. **Run the Django server**:
   ```sh
   cd server
   python manage.py runserver
   ```
   Visit `http://127.0.0.1:8000/` in your web browser to see the homepage.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes. Ensure that your code follows the project's coding standards and include tests where appropriate.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Feel free to explore the code and suggest improvements. Happy coding!
