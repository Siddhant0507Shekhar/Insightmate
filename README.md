# Insightmate: Chatbot with React.js and Django
Insightmate is a self-developed chatbot project that utilizes the power of Open AI API to provide an interactive and engaging chatbot experience. This project combines the frontend framework React.js with the backend framework Django to create a fully responsive chatbot website. You can use it using [this link](https://siddhantshekhar.pythonanywhere.com/). **If website doesn't load at first time please load it again. As it is deployed on python anywhere so it has limitations as of now** 

## Features
The Insightmate chatbot project offers the following features:

* **Fully Responsive Design:** The website is designed to be responsive and compatible with various devices, ensuring a seamless user experience on desktops, tablets, and mobile devices.

* **User Authentication:** The project includes a complete user authentication system that allows users to register, log in, and securely authenticate using tokens. This ensures that only authorized users can access the chatbot functionality.

* **Topic-wise Chats Saving:** When authenticated, the chatbot saves the user's conversations with different topics, allowing users to revisit previous chats and continue conversations seamlessly.

* **React Frontend:** The frontend of the Insightmate chatbot is developed using React.js. It includes three main components: Navbar, Sidebar, and Chatbar. These components are connected using various React hooks, enabling smooth communication and dynamic updates.

* **Django Backend:** The backend of the chatbot is built using the Django framework. It provides a robust and scalable infrastructure to handle user authentication, data storage, and API integration. The seamless API integration is achieved through the Django Rest Framework.

## Installation
To run Insightmate locally, follow these steps:

##### Clone the repository:

```bash
git clone https://github.com/Siddhant0507Shekhar/Insightmate
```

Navigate to the project directory:

```bash
cd Insightmate
```
#### Install the required dependencies for the frontend:
```bash
pip install -r requirements.txt
```
#### Then apply migrations 
```bash
python manage.py makemigrations
```
```bash
python manage.py migrate
```



#### Configure the environment variables:

Create a .env file in the backend directory.
Specify the required environment variables, such as API keys and database credentials, in the .env file.
Run the development server:


#### Finally navigate to the main project directory and start the Django development server:

```bash
cd Insightmate
python manage.py runserver
```
Access the Insightmate chatbot in your web browser at http://localhost:8000.

## Technologies Used
Insightmate incorporates the following technologies:

* React.js: A popular JavaScript library for building user interfaces.
* Django: A high-level Python web framework that simplifies development and promotes clean design.
* Django Rest Framework: A powerful and flexible toolkit for building Web APIs.
* Open AI API: The Open AI API powers the chatbot's conversational capabilities.
* HTML and CSS: The standard web development languages for structuring and styling webpages.

## Future Enhancements
Future enhancements for Insightmate could include:

* Natural Language Processing (NLP): Implementing advanced NLP techniques to improve the chatbot's understanding and response generation.
* Integration with External Services: Integrating the chatbot with external services or APIs to provide additional functionality or information.
* Multi-Language Support: Adding support for multiple languages to make the chatbot accessible to a broader audience.
* Admin Dashboard: Developing an admin dashboard to manage user accounts, conversations, and chatbot behavior.
* Contributing
* Contributions to Insightmate are welcome! If you have suggestions, bug reports, or would like to contribute new features
