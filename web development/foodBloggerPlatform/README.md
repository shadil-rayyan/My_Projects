![StackUp Banner]([https://tinkerhub.frappe.cloud/files/stackup%20banner.jpeg])
# Food Blogging site
This blog is built is for local blogging puropose on the topic of food this blog can 
## Team members
1. Shadil Am :[(https://github.com/shadil-rayyan)]
2. Adhitya Km : [(https://github.com/Adhithyakm)]
## Team Id
Team id here : cs-108
## Link to product walkthrough
[link to video]
## How it Works ?
##the code database is not woring due to an error
1. Explaining the working of project:
  the user can login in and publish post using write when opening there wont post any you need to write your own to display it on your home screen,you need to llogin to write/publish the post 
Backend (Node.js with Express):
Server Setup:
The Express app is initialized to handle server-side operations.
Middleware is set up to easily parse incoming JSON data and handle cookies.
File Uploads:
File Upload Endpoint:
An API endpoint (/api/upload) is established to deal specifically with file uploads.
When a file is uploaded, the endpoint responds with the filename in a JSON format.
Frontend (React.js):
Components:
The React app is organized into various components like Menu, Single, and Write, making it modular and maintainable.
Routing:
React Router, with features like useNavigate and Link from "react-router-dom," is employed for smooth client-side navigation between different pages.
State Management:
React's useState and useEffect hooks are utilized for managing component state.
These hooks help in handling side effects, such as fetching data from the server.
Axios:
Axios, a powerful HTTP client library, is integrated into the app to facilitate making HTTP requests from the frontend to the backend API.
Database (MongoDB):
Mysql serves as the database to store user and post-related data.
Specific database interactions, while not entirely visible in the provided snippets, are likely present in the application logic.
Styling (CSS):
CSS is emloyed to define the visual presentation of components, ensuring an aesthetically pleasing layout, color scheme, and responsiveness.
Authentication (Authentication Routes):
Authentication routes (authRoutes) are implemented to handle user registration, login, and potentially logout functionalities.
Client-Server Communication:
API endpoints (/api/auth, /api/users, /api/posts) act as bridges for communication between the frontend and backend.
These endpoints manage CRUD operations (Create, Read, Update, Delete) for users and posts, ensuring seamless data interaction.
4. Embed video of project demo
## Libraries used
#client side 
 "@testing-library/jest-dom": "^5.16.4",/
    "@testing-library/react": "^13.1.1",
    "@testing-library/user-event": "^13.5.0",
    "axios": "^0.27.2",
    "dompurify": "^2.4.0",
    "moment": "^2.29.4",
    "react": "^18.0.0",
    "react-dom": "^18.0.0",
    "react-quill": "^2.0.0",
    "react-router-dom": "^6.4.1",
    "react-scripts": "5.0.1",
    "sass": "^1.55.0",
    "web-vitals": "^2.1.4" 
#api 
    "bcryptjs": "^2.4.3",
    "cookie-parser": "^1.4.6",
    "express": "^4.18.1",
    "jsonwebtoken": "^8.5.1",
    "multer": "^1.4.5-lts.1",
    "mysql": "^2.18.1",
    "nodemon": "^2.0.20"

## How to configure
git clone the resporitry using git clone link (you need to install git )
after go to client folder in cmd and run npm install or yarn (to use yarn install it using npm install --global yarn)
go to api folder in cmd and run npm install or yarn
## How to Run
run the api folder using npm start 
after open another a command prompt and run npm start in folder client 

