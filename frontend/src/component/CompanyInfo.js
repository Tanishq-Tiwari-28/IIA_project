import React from "react";
import { Link } from "react-router-dom";
// import Contact from '../page/Contact'

const CompanyInfo = () => {
  return (
    <div>
      <section className="pt-10">
        <div
          className="container pt-4 mx-auto bg-white sm:p-6 lg:p-8 rounded-lg bg-white"
          style={{ maxWidth: "90%", boxShadow: "0 0 40px rgba(0, 0, 0, 0.5)" }}
        >
          <div className="flex flex-wrap mx-auto">
            <div className="w-full px-8 lg:w-1/2">
              <div className="pb-12 mb-12 mx-2 border-b lg:mb-0 lg:pb-0 lg:border-b-0">
                <h2 className="mb-4 text-3xl font-bold lg:text-4xl font-heading text-orange-600">
                  Requirement & Use cases
                </h2>
                <p className="mb-8 leading-loose text-gray-500 dark:text-black">
                  There is no single data source which could provide all sort of
                  information related to drugs, like their scientific values,
                  effectiveness, use cases, symptoms. This data is spreaded over
                  multiple databases mentioned above.But when a user and
                  researcher wants to study about it, either they couldn’t get
                  all the necessary information or they have to put extra time
                  and efforts to explore the web. This application will be one
                  shot place to all their needs and requirements.
                </p>
                <div className="w-full md:w-1/3">
                  <Link to={"Contact"}>
                    <button
                      type="button"
                      className="py-2 px-4 mx-auto bg-orange-600 hover:bg-orange-700 focus:ring-orange-600 focus:ring-offset-orange-200 text-slate-100 w-full transition ease-in duration-200 text-center text-base font-semibold drop-shadow-4xl box-shadow-6xl focus:outline-none focus:ring-2 focus:ring-offset-2  rounded-lg "
                    >
                      Contact us
                    </button>
                  </Link>
                </div>
              </div>
            </div>
            <div className="w-full px-8 lg:w-1/2">
              <ul className="space-y-1">
                <li className="flex -mx-4">
                  <div className="px-4 ">
                    <span className="flex items-center justify-center w-16 h-16 mx-auto text-2xl font-bold text-orange-600 rounded-full font-heading bg-gray-100">
                      1
                    </span>
                  </div>
                  <div className="px-4">
                    <h3 className="my-2 text-3xl font-bold text-orange-600">
                      Compound Information Retrieval
                    </h3>
                    <p className="leading-loose text-gray-500 dark:text-black">
                      Users can input compound names, attributes, or IDs, and
                      the platform will retrieve and display comprehensive
                      compound information from various databases.
                    </p>
                  </div>
                </li>
                <li className="flex -mx-4">
                  <div className="px-4">
                    <span className="flex items-center justify-center w-16 h-16 mx-auto text-2xl font-bold text-orange-600 rounded-full font-heading bg-gray-100">
                      2
                    </span>
                  </div>
                  <div className="px-4">
                    <h3 className="my-2 text-3xl font-bold text-orange-600">
                      Research and Study
                    </h3>
                    <p className="leading-loose text-gray-500 dark:text-black">
                      Researchers and students can access detailed compound
                      information for academic projects, research papers, and
                      studies using the platform.
                    </p>
                  </div>
                </li>
                <li className="flex -mx-4">
                  <div className="px-4">
                    <span className="flex items-center justify-center w-16 h-16 mx-auto text-2xl font-bold text-orange-600 rounded-full font-heading bg-gray-100">
                      3
                    </span>
                  </div>
                  <div className="px-4">
                    <h3 className="my-2 text-3xl font-bold text-orange-600">
                      EComparison and Analysis
                    </h3>
                    <p className="leading-loose text-gray-500 dark:text-black">
                      Users can input multiple compound names to compare and
                      analyze their properties, aiding in decision-making and
                      analysis.
                    </p>
                  </div>
                </li>
              </ul>
            </div>
          </div>
        </div>
      </section>
    </div>
  );
};

export default CompanyInfo;
