import React, { useState } from 'react';
import './OnlineConsultation.css';

function OnlineConsultation() {
  // Initial form state with fields for the appointment
  const [formData, setFormData] = useState({
    firstName: '',
    lastName: '',
    email: '',
    phone: '',
    reason: '',
    appointmentDate: '',  // Added
    appointmentTime: ''   // Added
  });

  // State to store the confirmation message after form submission
  const [message, setMessage] = useState('');

  // Handler to update form state when input fields change
  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prevState => ({
      ...prevState,
      [name]: value
    }));
  };

  // Handler to process form data when form is submitted
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

    // Set the confirmation message with link to the online meeting
    setMessage(`
  You have been invited to an online meeting.<br/>
  Click to <a href="https://chime.aws/1508622372" target="_blank" rel="noopener noreferrer">join the meeting</a>.<br/>
  Meeting ID: 1508622372
`);

  };

  return (
    <div className="online-consultation-container">
      <h1>Appointment Counseling Form</h1>
      
      
      {/* {message && <div className="confirmation-message">{message}</div>} */}
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
      {message && <div className="confirmation-message" dangerouslySetInnerHTML={{ __html: message }}></div>}
    </div>
  );
}

export default OnlineConsultation;
