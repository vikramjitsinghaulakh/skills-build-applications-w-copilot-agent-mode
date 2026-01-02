
import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import App from './App';
import reportWebVitals from './reportWebVitals';

// Set REACT_APP_CODESPACE_NAME from window.env if available
if (!process.env.REACT_APP_CODESPACE_NAME && window.env && window.env.REACT_APP_CODESPACE_NAME) {
  process.env.REACT_APP_CODESPACE_NAME = window.env.REACT_APP_CODESPACE_NAME;
}

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);

reportWebVitals();
