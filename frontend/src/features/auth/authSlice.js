import { createSlice } from '@reduxjs/toolkit';

export const authSlice = createSlice({
    name: 'auth',
    initialState: {},
    reducers: {
        setUser: (state, action) => {
            return action.payload;
        }
    }
});

export const { setUser } = authSlice.actions;

export default authSlice.reducer;