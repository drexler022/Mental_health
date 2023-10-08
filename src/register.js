// register.js

import React, { useState } from 'react';
import './OnlineConsultation.css';

function Register() {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [url, setUrl] = useState('');  
    const [error, setError] = useState(false);
  
    const handleSubmit = () => {
      if (username !== 'doctor' || password !== 'mentalhealth') {
        setError(true);
      } else {
        setError(false);
        
      }
    };
  
    return (
      <div>
        <div>
          <label>Account Name:</label>
          <input 
            type="text" 
            value={username} 
            onChange={(e) => setUsername(e.target.value)} 
          />
        </div>
        <div>
          <label>Password:</label>
          <input 
            type="password" 
            value={password} 
            onChange={(e) => setPassword(e.target.value)} 
          />
        </div>
        <div>
          <label>URL:</label>  {/* 新增 URL 输入栏 */}
          <input 
            type="text" 
            value={url} 
            onChange={(e) => setUrl(e.target.value)} 
          />
        </div>
        <button onClick={handleSubmit}>Register</button>
        {error && <div className="confirmation-message">Wrong accountname or password!</div>}
      </div>
    );
  }
  
  export default Register;
