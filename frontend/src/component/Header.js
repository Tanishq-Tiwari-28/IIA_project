import React, { useState, useEffect } from 'react';
import logo from "../assets/bioSyncLogo.png";
import { Link } from "react-router-dom";
import { FaChalkboardTeacher } from "react-icons/fa";
import {AiOutlineMail} from "react-icons/ai"
// import { FcCallback } from "react-icons/fc";
// import { useDispatch } from 'react-redux';
// import { logoutRedux } from '../redux/userSlice';
// import { toast } from 'react-hot-toast';
// import { Toaster } from 'react-hot-toast';
// import contactHome from "../assets/contactHome.png"


const Header = () => {
  const [isOpen, setIsOpen] = useState(false);
  const [isMobileView, setIsMobileView] = useState(window.innerWidth < 768);

  const handleToggleMenu = () => {
    setIsOpen(!isOpen);
  };

  useEffect(() => {
    // Update the state when the window is resized
    const handleWindowResize = () => {
      setIsMobileView(window.innerWidth < 768);
    };

    window.addEventListener('resize', handleWindowResize);

    return () => {
      window.removeEventListener('resize', handleWindowResize);
    };
  }, []);
  return (
    <nav className="shadow bg-gray-50 dark:bg-gray-900" >
      <div className="container px-3 pb-2 pt-3 mx-auto">
        <div className="lg:flex lg:items-center ">
          <div className="flex items-center justify-between">
            <div className='flex'>
              {/* Company Logo */}
              <div className='h-20 w-30'>
                <Link to={"/"}>
                  <img src={logo} alt='logo' className='h-full w-full' />
                </Link>
              </div>

              {/* Company Name and Address */}
              <div style={{ display: 'flex', flexDirection: 'column', paddingLeft: '15px' }}>
                
                  <div className={`text-gray-900 dark:text-slate-200 ${isOpen || isMobileView ? 'text-3xl' : 'text-3xl'} font-base leading-right`} style={{ fontFamily: 'VintageFont', paddingBottom: '0px', paddingTop: '8px' }}>
                    IIA Project
                  </div>
                
                
                  <div className={`text-gray-900 dark:text-slate-200 ${isOpen || isMobileView ? 'text-xs' : 'text-base'} flex items-center`} style={{ fontFamily: 'VintageFont' }}>
                    <FaChalkboardTeacher />
                    <div className='px-2' >Prof: Dr. Mukesh mohania</div>
                  </div>
                
                <div />
              </div>
            </div>

            {/* Mobile menu button */}
            <div className="flex lg:hidden">
              <button
                type="button"
                className="text-gray-500 dark:text-gray-200 hover:text-gray-600 dark:hover:text-gray-400 focus:outline-none focus:text-gray-600 dark:focus:text-gray-400"
                aria-label="toggle menu"
                onClick={handleToggleMenu}
              >
                {!isOpen ? (
                  <svg xmlns="http://www.w3.org/2000/svg" className="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth="2">
                    <path strokeLinecap="round" strokeLinejoin="round" d="M4 8h16M4 16h16" />
                  </svg>
                ) : (
                  <svg xmlns="http://www.w3.org/2000/svg" className="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth="2">
                    <path strokeLinecap="round" strokeLinejoin="round" d="M6 18L18 6M6 6l12 12" />
                  </svg>
                )}
              </button>
            </div>
          </div>

          {/* Mobile menu */}
          <div className={`${isOpen ? 'block' : 'hidden'} mt-4 lg:flex lg:items-center lg:w-auto lg:mt-0 lg:bg-transparent lg:px-6 lg:py-4 lg:opacity-100 lg:relative lg:flex-1 lg:justify-between`}>
            <div className="flex flex-col text-gray-900 capitalize dark:text-gray-300 lg:flex lg:px-16 lg:-mx-4 lg:flex-row lg:items-center">
              <Link to={""} className={`mt-2 transition-colors duration-300 transform lg:mt-0 lg:mx-4 ${isMobileView ? 'text-2xl' : 'text-base'} ${isOpen || isMobileView ? 'text-xl' : ''} hover:text-gray-900 dark:hover:text-orange-600 hover:text-orange-600`}>
                Home
              </Link>
              <Link to={"milestones"} className={`mt-2 transition-colors duration-300 transform lg:mt-0 lg:mx-4 ${isMobileView ? 'text-2xl' : 'text-base'} ${isOpen || isMobileView ? 'text-xl' : ''} hover:text-gray-900 dark:hover:text-orange-600 hover:text-orange-600`}>
                Mile Stones
              </Link>
              <Link to={"team"} className={`mt-2 transition-colors duration-300 transform lg:mt-0 lg:mx-4 ${isMobileView ? 'text-2xl' : 'text-base'} ${isOpen || isMobileView ? 'text-xl' : ''} hover:text-gray-900 dark:hover:text-orange-600 hover:text-orange-600`}>
                Team
              </Link>

            </div>
            
            
          </div>

            <div className="flex felx-row gap-7 px-5" style={{paddingRight:"50px"}}>
                {/* Youtube link for VK welding */}
                <Link to={"#"} >
                <div className="group">
                    <AiOutlineMail className="w-20px h-20px text-xl text-gray-400 transition-colors duration-200 hover:text-gray-800 dark:hover:text-orange-600" />
                    <div className="hidden group-hover:block absolute -mt-8 ml-2 bg-gray-800 text-gray-400 text-xs p-1 rounded shadow-lg">
                    Tanishq
                    </div>
                </div>
                </Link>

                {/* Google search for VK welding works */}
                <Link
                to={"mailto:aniket21448@iiitd.ac.in"}
                target="_blank"
                
                >
                <div className="group">
                    <AiOutlineMail className="w-20px h-20px text-xl text-gray-400 transition-colors duration-200 hover:text-gray-800 dark:hover:text-orange-600" />
                    <div className="hidden group-hover:block absolute -mt-8 ml-2 bg-gray-800 text-gray-400 text-xs p-1 rounded shadow-lg">
                    Aniket
                    </div>
                </div>
                </Link>

                {/* Map location for VK welding works */}
                <Link
                to={"#"}
                target="_blank"
                
                >
                <div className="group">
                    <AiOutlineMail className="w-20px h-20px text-xl text-gray-400 transition-colors duration-200 hover:text-gray-800 dark:hover:text-orange-600" />
                    <div className="hidden group-hover:block absolute -mt-8 ml-2 bg-gray-800 text-gray-400 text-xs p-1 rounded shadow-lg">
                    Siddartha
                    </div>
                </div>
                </Link>

            </div>
        </div>
      </div>
      {/* <Toaster /> */}
    </nav>
  );
};

export default Header;
