
import { createSlice } from '@reduxjs/toolkit'

const initialState = {
    productList:[]    
}
export const productSlice = createSlice({
    name : "product",
    initialState,

    reducers : {
        setProductData : (state, action)=>{
            // console.log(action)
            state.productList = [...action.payload]
        }
    }
})

export const {setProductData} = productSlice.actions

export default productSlice.reducer