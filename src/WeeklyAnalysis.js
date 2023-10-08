import React from 'react';

function WeeklyAnalysis() {
  return (
    <div className="weekly-analysis">
      <h2>Weekly Analysis</h2>
      <div className="image-container">
        <img src="/bigram.png" alt="Bigram" style={{ maxWidth: "90%", maxHeight: "500px" }}/>
        <img src="/emergency word.png" alt="Emergency Word" style={{ maxWidth: "90%", maxHeight: "500px" }}/>
        <img src="/frequency.png" alt="Frequency" style={{ maxWidth: "90%", maxHeight: "500px" }}/>
        <img src="/sentiment progression.png" alt="Sentiment Progression 1" style={{ maxWidth: "90%", maxHeight: "500px" }}/>
        <img src="/sentiment progression2.png" alt="Sentiment Progression 2" style={{ maxWidth: "90%", maxHeight: "500px" }}/>
        <img src="/tfidf.png" alt="TFIDF" style={{ maxWidth: "90%", maxHeight: "500px" }}/>
      </div>
    </div>
  );
}

export default WeeklyAnalysis;
