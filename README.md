# OptiRoute

OptiRoute is a mobile application designed to streamline your shopping experience by determining the most cost-effective route for purchasing items. It employs Traveling Salesman Problem and optimization techniques to find the most cost-efficient round trip route for purchasing items, minimizing the overall monetary cost.

## Table of Contents

- [Route Finder](#route-finder)
- [Route Visualizer](#route-visualizer)
- [Tech Stack](#tech-stack)
- [Getting Started](#getting-started)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Contributing](#contributing)
- [Collaborators](#collaborators)

## Route Finder

The Path Finder section utilizes the Haversine formula to calculate the distance between two points, taking into account the curvature of the Earth. It employs the total cost as a heuristic, which includes the cost of the item in each shop added to the cost of traveling to that particular shop. The latter is the product of Haversine distance and cost factor.

This heuristic-driven approach utilizes the Traveling Salesman Problem (TSP) and optimization techniques to identify the optimal round trip route that minimizes the combined monetary cost of both transportation and procurement.

## Route Visualizer

The Route Visualizer maps the coordinates of the most optimal route found by the Route Finder on the map using the react-native-maps library. It generates Google Maps URLs, allowing users to navigate to designated locations using provided coordinates.

## Tech Stack

OptiRoute is developed using the following technologies:

- React Native: The mobile application is built using React Native , providing a cross-platform development environment.

- Flask: The backend server is implemented using Flask, a lightweight web framework for Python.

- PostgreSQL: PostgreSQL is used as the database for storing and managing data related to the application.

# Getting Started

To get started with the project, clone the repository and install the necessary dependencies.

## Prerequisites

Before you begin, ensure you have the following prerequisites installed on your local development environment:

- Node.js: Ensure you have Node.js installed. You can download it from [here](https://nodejs.org/).

- Expo CLI: OptiRoute is built using Expo. If you don't have Expo CLI installed, you can install it globally using the following command:

  ```sh
  npm install -g expo-cli

## Installation

Follow these steps to set up and run OptiRoute on your local machine:

1. Clone the repository:

    ```sh
    git clone https://github.com/yashharne/OptiRoute.git
    ```

2. Navigate to the project directory:

    ```sh
    cd OptiRoute
    ```

3. Install dependencies:

    ```sh
    npm install
    ```

4. Start the Expo development server:

    ```sh
    expo start
    ```

5. Open the Expo Go app on your mobile device and scan the QR code displayed in the terminal.

6. The OptiRoute app will load on your device, and you can now explore the most cost-effective routes for your shopping needs!



# Contributing

We welcome contributions from the community to make OptiRoute even better. If you'd like to contribute, please follow these steps:

1. **Fork the Project**: Click the "Fork" button at the top right corner of the repository to create your copy.

2. **Clone your Fork**: Clone the repository to your local machine using the following command, replacing `<your-username>` with your GitHub username:

    ```sh
    git clone https://github.com/<your-username>/OptiRoute.git
    ```

3. **Create a Branch**: Create a new branch for your feature or bug fix:

    ```sh
    git checkout -b feature/AmazingFeature
    ```

4. **Make Changes**: Make your desired changes and commit them:

    ```sh
    git add .
    git commit -m 'Add some AmazingFeature'
    ```

5. **Push to Your Branch**: Push your changes to your forked repository:

    ```sh
    git push origin feature/AmazingFeature
    ```

6. **Open a Pull Request**: Go to the original repository on GitHub and open a pull request to the `main` branch.

Once your changes are reviewed and approved, they will be merged into the main project.


# Collaborators

- Yash Harne ([@yashharne](https://github.com/yashharne)) 
- Kanishka Bansode ([@kb-0311](https://github.com/kb-0311)) 
- Ashu Mittal ([@Ashu-0202](https://github.com/Ashu-0202)) 
- Naman Arora ([@Naman-1473](https://github.com/Naman-1473))

