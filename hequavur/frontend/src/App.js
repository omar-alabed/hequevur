import './App.css';

import {Home} from './components/Home';
import {Department} from './components/Department';
import {Candidate} from './components/Candidate';
import {Navigation} from './components/Navigation';

import {BrowserRouter, Route, Routes} from 'react-router-dom';

function App() {
  return (
    <BrowserRouter>
    <div className="container">
     <h3 className="m-3 d-flex justify-content-center">
       Hequavor
     </h3>

     <Navigation/>

     <Routes>
       <Route path='/' element={<Home/>} exact/>
       <Route path='/department' element={<Department/>}/>
       <Route path='/candidate' element={<Candidate/>}/>
     </Routes>
    </div>
    </BrowserRouter>
  );
}

export default App;