import React, { useState, useEffect, useMemo } from 'react';
import researchImg from "../assets/researchSearch.jpg"
import personalImg from "../assets/personalSearchButton.jpg"
import toast, { Toaster } from 'react-hot-toast';

const Hero = () => {
  const images = useMemo(() => [
    // Add your background images here
    researchImg,
    personalImg

  ], []);

  const [currentImage, setCurrentImage] = useState(0);
  const [loading, setLoading] = useState(true);
  const [isHovered, setIsHovered] = useState(false);

  // State to track form values
  const [formValues, setFormValues] = useState({
    searchType: 'pubchemID', // Default search type
    searchQuery: '',
    symptomsQuery: '',
  });

  // State to track form validity
  // eslint-disable-next-line
  const [isFormValid, setIsFormValid] = useState(false);

  useEffect(() => {
    const changeImage = () => {
      if (!isHovered) {
        setCurrentImage((prevImage) => (prevImage + 1) % images.length);
      }
    };

    const interval = setInterval(changeImage, 5000);

    return () => clearInterval(interval);
  }, [images.length, isHovered]);

  useEffect(() => {
    Promise.all(images.map((src) => loadImage(src))).then(() => {
      setLoading(false);
    });
  }, [images]);

  const loadImage = (src) => {
    return new Promise((resolve, reject) => {
      const img = new Image();
      img.onload = resolve;
      img.onerror = reject;
      img.src = src;
    });
  };

  const handleSliderHover = () => {
    setIsHovered(true);
  };

  const handleSliderLeave = () => {
    setIsHovered(false);
  };

  const handleInputChange = (event) => {
    const { name, value } = event.target;
    setFormValues({
      ...formValues,
      [name]: value,
    });
  };

  // Check if any of the required form fields are empty
  useEffect(() => {
    // eslint-disable-next-line
    const { searchType, searchQuery, symptomsQuery } = formValues;
    const isValid = searchQuery.trim() !== '' || symptomsQuery.trim() !== '';
    setIsFormValid(isValid);
  }, [formValues]);

  const handleSubmit = (event) => {
    event.preventDefault();
    // Handle form submission logic here
    toast.success("Searching !!!")
    // console.log('Form submitted with values:', formValues);
  };

  return (
    <div style={{ justifyContent: 'center', boxShadow: '0 29px 52px rgba(0,0,0,0.40), 0 25px 16px rgba(0,0,0,0.20)' }}>
      <header style={{ height: '38rem' }}>
        <Toaster />
        <div
          className="hero-slider"
          style={{
            backgroundImage: `url(${images[currentImage]})`,
            backgroundSize: 'cover',
            backgroundPosition: 'center',
            height: '100%',
            position: 'relative',
            borderRadius: '5px',
            overflow: 'hidden',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            transition: 'background-image 1s ease-in-out',
          }}

          onMouseEnter={handleSliderHover}
          onMouseLeave={handleSliderLeave}
        >


          {loading && <div>Loading...</div>}


          <div className="relative z-10 text-center">
            <div className="mx-10 sm:mx-20 md:mx-40 lg:mx-80">
              <h2 className="text-3xl sm:text-4xl md:text-5xl lg:text-6xl font-semibold text-white ">
                You think we <span className="text-orange-600 dark:text-orange-600">FIND IT</span>
              </h2>
              <p className="mt-4 text-base sm:text-lg md:text-xl text-white font-medium dark:text-grey-400 px-4 sm:px-8 md:px-10 lg:px-10 xl:px-0">
              We're creating a platform for users to search chemical compounds and access detailed information from databases like PubChem, ChemBL, and DrugBank. The user-friendly frontend will present the data effectively.
              </p>
            </div>


            <div className="max-w-3xl mx-auto px-6  py-5">
            <div className="flex flex-col gap-8 items-center">
              <form onSubmit={handleSubmit} >

              <div className="flex flex-row gap-5">

                <select
                  id="searchType"
                  name="searchType"
                  value="searchType"
                  onChange={handleInputChange}
                  className="flex-1 px-4 py-2 mb-2 text-gray-700  border rounded-md dark:bg-gray-900 dark:text-gray-400 dark:border-gray-600 focus:border-blue-400 dark:focus:border-blue-300 focus:outline-none focus:ring focus:ring-blue-300 focus:ring-opacity-40"
                >
                  <option value="NA">Select ID type</option>
                  <option value="pubchemID">Pubchem ID</option>
                  <option value="chmbLID">ChmbL ID</option>
                  <option value="drugbankID">Drugbank ID</option>
                </select>
              </div>

              <div className="flex flex-col gap-3 sm:flex-row sm:justify-center sm:-mx-0">
                <input
                  id="text"
                  type="text"
                  className="flex-1 px-4 py-2 mb-2 text-gray-700 bg-white border rounded-md dark:bg-gray-900 dark:text-gray-300 dark:border-gray-600 focus:border-blue-400 dark:focus:border-blue-300 focus:outline-none focus:ring focus:ring-blue-300 focus:ring-opacity-40"
                  placeholder="Search the drug"
                />
              </div>


              <textarea
                  placeholder="Describe your symptoms"
                  className="w-full h-32 px-4 py-2.5 text-gray-700 bg-white border rounded-lg dark:bg-gray-900 dark:text-gray-300 dark:border-gray-600 focus:border-blue-400 dark:focus:border-blue-300 focus:outline-none focus:ring focus:ring-blue-300 focus:ring-opacity-40"
                ></textarea>


                <p className="mt-0  mb-4 text-m text-gray-400 dark:text-gray-200">We will search based on your inputs</p>
              <div>
                <button className="px-6 py-2 font-medium tracking-wide text-white capitalize transition-colors duration-300 transform bg-orange-600 rounded-lg hover:bg-orange-700 focus:outline-none focus:ring focus:ring-orange-300 focus:ring-opacity-80">
                  Search
                </button>
              </div>

              </form>
            </div>
          </div>


          </div>

        </div>
      </header>
    </div>
  );
};

export default Hero;







