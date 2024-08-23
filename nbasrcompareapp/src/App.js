import logo from './logo.svg';
import './App.css';
import React from "react"
import Axios from "axios"
import Cookies from 'js-cookie'
const csrftoken=Cookies.get('csrftoken')
let comparison=""
const getcomparison = (data)=>{comparison=data}
function getplayernames(p1,p2){
  Axios.post('http://127.0.0.1:8000/dbapi/',
    {player1name:p1,
    player2name:p2}).then(function(response){
        getcomparison(response.data);
        console.log(response.data.comparison)
        document.getElementById('comparison').innerHTML=response.data.comparison
    })
}


function App() {
  return (
      <div>
          <input id="selectp1" type="text" autoComplete="on" list="p1"/> 
          <datalist id="p1">
              <option>Kyrie Irving</option>
              <option>Stephen Curry</option>
          </datalist>
          <input id="selectp2" type="text" autoComplete="on" list="p2"/> 
          <datalist id="p2">
            <option>Kyrie Irving</option>
            <option>Stephen Curry</option>
          </datalist>
          <div id="comparison">hello</div>
          <button type="button" onClick={() => {
            getplayernames(document.getElementById("selectp1").value,document.getElementById("selectp2").value);
          }}>compare</button>
      </div>
      
  );
}

export default App;
