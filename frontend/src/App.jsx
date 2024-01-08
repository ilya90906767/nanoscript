import React from 'react';
import MainPage from './components/pages/MainPage.js'
import { BrowserRouter, Route, Routes } from 'react-router-dom';

function App() {
 return (
 <BrowserRouter>
 <Routes>
    <Route exact path="/" element={<MainPage/>} />
 </Routes>
</BrowserRouter>
 );
}

export default App;