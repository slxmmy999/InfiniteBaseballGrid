# Infinite Immaculate Grid

## About the Project
[Infinite Immaculate Grid](https://www.infiniteimmaculategrid.com/) is an unlimited open source clone of the popular daily baseball trivia game [Immaculate Grid](https://www.immaculategrid.com/). The goal of this project is to create a community-driven, open source version of Immaculate Grid that anyone can contribute to. The project is built using [NuxtJS](https://nuxtjs.org/) for the frontend and [Quart](https://pgjones.gitlab.io/quart/) (Python) for the backend. The project is hosted on [Vercel](https://vercel.com/) and [Heroku](https://www.heroku.com/).

## Contributing

We welcome contributions from everyone. Here's how you can contribute:

### Forking and Cloning the Repository

1. **Fork the Repository**: Start by forking this repository to your own GitHub account. You can do this by clicking the "Fork" button at the top right corner of this page.

2. **Clone the Repository**: After forking the repository, you'll need to clone it to your local machine to make changes. Click the "Code" button on your forked repository and copy the URL.

    Open a terminal on your local machine and run the following git command:

    ```bash
    git clone "url-you-just-copied"
    ```

    Replace `"url-you-just-copied"` with the URL of your forked repository. It should look something like this:

    ```bash
    git clone https://github.com/your-username/InfiniteImmaculateGrid.git
    ```

3. **Navigate into the Directory**: Now navigate into the cloned directory:

    ```bash
    cd InfiniteImmaculateGrid
    ```

4. **Create a New Branch**: Create a new branch where you'll make your changes. You can create a branch with the following command:

    ```bash
    git checkout -b your-new-branch-name
    ```

    Replace `"your-new-branch-name"` with a name that describes the changes you're planning to make.

5. **Make Your Changes**: Now you're ready to make your changes! Open up the project in your favorite text editor and get to work.

Remember, once you've made your changes, you'll need to commit them, push them to your forked repository, and then open a pull request. We'll review your changes and, if everything looks good, merge them into the main project.


## Getting Started

### Set the development variables

The frontend and backend both have variables that need to be changed in order to set the project to "development mode", which configures the project to run correctly in your local environment. Here's how you can get the project ready to run on your machine:

1. Set `env` variable in the file [`nuxt.config.js`](nuxt.config.js) to `"dev"` like so:
   ```js
   const env = "dev";
   ```

2. Set the `dev` variable in the file [`server/server.py`](server/server.py) to `True` like so:
    ```py
    dev = True
    ```

### Install Python and Node requirements

```bash
# Install Python requirements
pip install -r requirements.txt

# Install Node modules
npm install
```

### Run the NuxtJS frontend

```bash
# Start the hot-reloading development server on localhost:3000
npm run dev
```

### Run the Quart backend
In a separate terminal window, run the following command to start the backend server:

```bash
python server/server.py
```

### Open the project in your browser

Open your browser and navigate to [localhost:3000](http://localhost:3000) to see the project running in your browser.

## Asking for Help

I strongly believe that anyone should be able to contribute to projects they care about, no matter their skill level or abilities. I am always here to help anyone who may need it so feel free to reach out to me with any questions you may have. If you need any help anywhere in the contribution process, you can ask for help in the [Discord Server](https://discord.gg/rPBuvhqG8p) or in the 
[GitHub Discussions](https://github.com/slxmmy999/InfiniteImmaculateGrid/discussions) 
section of this repository.
