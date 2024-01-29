/*
The Single component is a functional component that displays details of a single post.
It uses state (post) to store the fetched post data and the useEffect hook to fetch the
 data when the component mounts or when the postId changes.
It includes functions to handle post deletion (handleDelete) and to extract text content
 from HTML (getText).
The component renders the post details, including the post image, user information, 
edit/delete options for the post owner, post title, and sanitized post description.
The Menu component is also rendered, passing the post category as a prop
*/
// Import necessary dependencies from React and other libraries
import React, { useEffect, useState } from "react";
import Edit from "../img/edit.png";
import Delete from "../img/delete.png";
import { Link, useLocation, useNavigate } from "react-router-dom";
import Menu from "../components/Menu";
import axios from "axios";
import moment from "moment";
import { useContext } from "react";
import { AuthContext } from "../context/authContext";
import DOMPurify from "dompurify";

// Functional component named Single
const Single = () => {
  // State to store the post data
  const [post, setPost] = useState({});

  // Get the current location and navigate function from react-router-dom
  const location = useLocation();
  const navigate = useNavigate();

  // Extract the post ID from the URL
  const postId = location.pathname.split("/")[2];

  // Access the current user information from the AuthContext
  const { currentUser } = useContext(AuthContext);

  // useEffect hook to fetch post data when the component mounts or postId changes
  useEffect(() => {
    // Function to fetch post data asynchronously
    const fetchData = async () => {
      try {
        // Send a GET request to fetch the specific post using postId
        const res = await axios.get(`/posts/${postId}`);
        // Update the state with the fetched post data
        setPost(res.data);
      } catch (err) {
        // Log any errors that occur during the data fetching process
        console.log(err);
      }
    };
    // Call the fetchData function
    fetchData();
  }, [postId]);

  // Function to handle post deletion
  const handleDelete = async () => {
    try {
      // Send a DELETE request to delete the post with postId
      await axios.delete(`/posts/${postId}`);
      // Navigate to the home page after successful deletion
      navigate("/");
    } catch (err) {
      // Log any errors that occur during the deletion process
      console.log(err);
    }
  };

  // Function to extract text content from HTML using DOMParser
  const getText = (html) => {
    const doc = new DOMParser().parseFromString(html, "text/html");
    return doc.body.textContent;
  };

  // Render the component with post details and a Menu component
  return (
    <div className="single">
      <div className="content">
        {/* Render the post image */}
        <img src={`../upload/${post?.img}`} alt="" />
        <div className="user">
          {/* Render the user image if available */}
          {post.userImg && (
            <img
              src={post.userImg}
              alt=""
            />
          )}
          {/* Render user information (username, post date) */}
          <div className="info">
            <span>{post.username}</span>
            <p>Posted {moment(post.date).fromNow()}</p>
          </div>
          {/* Render edit and delete options for the post owner */}
          {currentUser.username === post.username && (
            <div className="edit">
              {/* Render the Edit icon as a link to the write page with edit mode */}
              <Link to={`/write?edit=2`} state={post}>
                <img src={Edit} alt="" />
              </Link>
              {/* Render the Delete icon with a click event to handle deletion */}
              <img onClick={handleDelete} src={Delete} alt="" />
            </div>
          )}
        </div>
        {/* Render post title */}
        <h1>{post.title}</h1>
        {/* Render post description with sanitized HTML using DOMPurify */}
        <p
          dangerouslySetInnerHTML={{
            __html: DOMPurify.sanitize(post.desc),
          }}
        ></p>
      </div>
      {/* Render the Menu component with the post category */}
      <Menu cat={post.cat} />
    </div>
  );
};

// Export the Single component as the default export
export default Single;
