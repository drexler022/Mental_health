import React from 'react';
import './App.css';
import { BrowserRouter as Router, Route, Link, Routes } from 'react-router-dom';
import Main from './Main';
import OnlineConsultation from './OnlineConsultation';
import WeeklyAnalysis from './WeeklyAnalysis';

function App() {
  return (
    <Router>
      <div>
        <nav>
          <ul>
            <li><Link to="/">Main</Link></li>
            <li><Link to="/online-consultation">Online Consultation</Link></li>
            <li><Link to="/weekly-analysis">Weekly Analysis</Link></li>
          </ul>
        </nav>

        <Routes>
          <Route path="/" element={<Main />} />
          <Route path="/online-consultation" element={<OnlineConsultation />} />
          <Route path="/weekly-analysis" element={<WeeklyAnalysis />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
