import React, { useState } from 'react';
import './OnlineConsultation.css';

function OnlineConsultation() {
  const [formData, setFormData] = useState({
    firstName: '',
    lastName: '',
    email: '',
    phone: '',
    reason: '',
    appointmentDate: '',  // Added
    appointmentTime: ''   // Added
  });

  const [message, setMessage] = useState('');

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prevState => ({
      ...prevState,
      [name]: value
    }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log(formData);

    // Clear the form data
    setFormData({
      firstName: '',
      lastName: '',
      email: '',
      phone: '',
      reason: '',
      appointmentDate: '',
      appointmentTime: ''
    });

    // Display the message
    setMessage("Appointment made, please wait for follow up contact.");
  };

  return (
    <div className="online-consultation-container">
      <h1>Appointment Counseling Form</h1>
      {message && <div className="confirmation-message">{message}</div>}
      <form onSubmit={handleSubmit}>
        <div>
          <label>First Name:</label>
          <input type="text" name="firstName" value={formData.firstName} onChange={handleChange} required />
        </div>
        <div>
          <label>Last Name:</label>
          <input type="text" name="lastName" value={formData.lastName} onChange={handleChange} required />
        </div>
        <div>
          <label>Email:</label>
          <input type="email" name="email" value={formData.email} onChange={handleChange} required />
        </div>
        <div>
          <label>Phone:</label>
          <input type="tel" name="phone" value={formData.phone} onChange={handleChange} required />
        </div>
        <div>
          <label>Reason for seeking help:</label>
          <textarea name="reason" value={formData.reason} onChange={handleChange} required></textarea>
        </div>
        <div>
          <label>Appointment Date:</label>
          <input type="date" name="appointmentDate" value={formData.appointmentDate} onChange={handleChange} required />
        </div>
        <div>
          <label>Appointment Time:</label>
          <input type="time" name="appointmentTime" value={formData.appointmentTime} onChange={handleChange} required />
        </div>
        <div>
          <button type="submit">Submit</button>
        </div>
      </form>
    </div>
  );
}

export default OnlineConsultation;
