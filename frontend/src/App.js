import React from 'react';
import Header from './component/Header'
import { Outlet } from 'react-router-dom';
import Footer from './component/Footer';


function App() {

  return (
    <div>
      <Header/>
        <main >
          <Outlet/>
        </main>
      <Footer />
    </div>
  );
}

export default App;