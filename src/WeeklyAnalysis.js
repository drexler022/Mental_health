import React, { useState } from 'react';


const AWS = require('aws-sdk');

AWS.config.update({
  accessKeyId: '',
  secretAccessKey: ''
});

function WeeklyAnalysis() {
  return <div className="weekly-analysis">Weekly Analysis Page Content</div>;
}

export default WeeklyAnalysis;
