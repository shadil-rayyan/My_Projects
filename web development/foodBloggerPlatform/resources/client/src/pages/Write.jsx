import React, { useState } from "react";
import ReactQuill from "react-quill";
import "react-quill/dist/quill.snow.css";
import axios from "axios";
import { useLocation, useNavigate } from "react-router-dom";
import moment from "moment";

const Write = () => {
  const state = useLocation().state;
  const [value, setValue] = useState(state?.title || "");
  const [title, setTitle] = useState(state?.desc || "");
  const [file, setFile] = useState(null);
  const [cat, setCat] = useState(state?.cat || "");

  const navigate = useNavigate()

  const upload = async () => {
    try {
      const formData = new FormData();
      formData.append("file", file);
      const res = await axios.post("/upload", formData);
      return res.data;
    } catch (err) {
      console.log(err);
    }
  };

  const handleClick = async (e) => {
    e.preventDefault();
    const imgUrl = await upload();

    try {
      state
        ? await axios.put(`/posts/${state.id}`, {
            title,
            desc: value,
            cat,
            img: file ? imgUrl : "",
          })
        : await axios.post(`/posts/`, {
            title,
            desc: value,
            cat,
            img: file ? imgUrl : "",
            date: moment(Date.now()).format("YYYY-MM-DD HH:mm:ss"),
          });
          navigate("/")
    } catch (err) {
      console.log(err);
    }
  };

  return (
    <div className="add">
      <div className="content">
        <input
          type="text"
          placeholder="Title"
          onChange={(e) => setTitle(e.target.value)}
        />
        <div className="editorContainer">
          <ReactQuill
            className="editor"
            theme="snow"
            value={value}
            onChange={setValue}
          />
        </div>
      </div>
      <div className="menu">
        <div className="item">
          <h1>Publish</h1>
          <span>
            <b>Status: </b> Draft
          </span>
          <span>
            <b>Visibility: </b> Public
          </span>
          <input
            style={{ display: "none" }}
            type="file"
            id="file"
            name=""
            onChange={(e) => setFile(e.target.files[0])}
          />
          <label className="file" htmlFor="file">
            Upload Image
          </label>
          <div className="buttons">
            <button>Save as a draft</button>
            <button onClick={handleClick}>Publish</button>
          </div>
        </div>
        <div className="item">
          <h1>Category</h1>
          <div className="cat">
            <input
              type="radio"
              checked={cat === "indian"}
              name="cat"
              value="indian"
              id="indian"
              onChange={(e) => setCat(e.target.value)}
            />
            <label htmlFor="art">Indian</label>
          </div>
          <div className="cat">
            <input
              type="radio"
              checked={cat === "ARABIAN"}
              name="cat"
              value="arabian"
              id="arabian"
              onChange={(e) => setCat(e.target.value)}
            />
            <label htmlFor="arabian">arabian</label>
          </div>
          <div className="cat">
            <input
              type="radio"
              checked={cat === "chinnesy"}
              name="cat"
              value="chinnesy"
              id="chinnesy"
              onChange={(e) => setCat(e.target.value)}
            />
            <label htmlFor="chinnesy">chinines</label>
          </div>
          <div className="cat">
            <input
              type="radio"
              checked={cat === "french"}
              name="cat"
              value="french"
              id="french"
              onChange={(e) => setCat(e.target.value)}
            />
            <label htmlFor="french">french</label>
          </div>
          <div className="cat">
            <input
              type="radio"
              checked={cat === "italian"}
              name="cat"
              value="italian"
              id="italian"
              onChange={(e) => setCat(e.target.value)}
            />
            <label htmlFor="italian">italian</label>
          </div>
          <div className="cat">
            <input
              type="radio"
              checked={cat === "mexician"}
              name="cat"
              value="mexician"
              id="mexician"
              onChange={(e) => setCat(e.target.value)}
            />
            <label htmlFor="mexician">mexician</label>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Write;
