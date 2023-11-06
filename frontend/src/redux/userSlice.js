import { createSlice } from "@reduxjs/toolkit";

const initialState = {

    _id:"",
    firstName:"",
    lastName:"",
    email:"",


}; // Corrected variable name

export const userSlice = createSlice({
  name: "user",
  initialState, // Corrected variable name
  reducers: {
    loginRedux: (state = initialState, action) => {
      console.log(action.payload.data); //prints the data corresponding to each user.
      state._id = action.payload.data._id
      state.firstName = action.payload.data.firstName
      state.lastName = action.payload.data.lastName
      state.email = action.payload.data.email


    },
    logoutRedux: (state = initialState, action) => {
        // console.log(action.payload.data); //prints the data corresponding to each user.
        state._id = ""
        state.firstName = ""
        state.lastName = ""
        state.email = ""
  
  
      },
  
},


});

export const { loginRedux, logoutRedux } = userSlice.actions;
export default userSlice.reducer;