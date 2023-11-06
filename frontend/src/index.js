import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import { createBrowserRouter, createRoutesFromElements, Route, RouterProvider } from 'react-router-dom'

import Home from "./page/Home";
import Team from "./page/Team";
import Milestones from './page/Milestones';
// import Products from "./page/Products";
// import Contact from "./page/Contact";
// import Login from "./page/Login";
// import Signup from './page/Signup';
// import Profile from './page/Profile';
// import Customproduct from './page/Customproduct'

import { store } from './redux/index'
import { Provider } from 'react-redux'

const router = createBrowserRouter(
  createRoutesFromElements(
    <Route path="/" element={<App />}>
      <Route index element={<Home />} />
      <Route path='milestones' element={<Milestones />} />
      <Route path='team' element={<Team />} />  
      {/* <Route path='contact' element={<Contact />} /> */}
      {/* <Route path='login' element={<Login />} /> */}
      {/* <Route path='signup' element={<Signup />} /> */}
      {/* <Route path='profile' element={<Profile />} /> */}
      {/* <Route path='customproduct' element={<Customproduct />} /> */}
    </Route>

  )
)

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <Provider store={store}>
    < RouterProvider router={router} />

  </Provider>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();