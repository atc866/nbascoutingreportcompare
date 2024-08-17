import logo from './logo.svg';
import './App.css';

function getplayernames(p1,p2){
  console.log(p1);
  console.log(p2);
}
function App() {
  return (
      <div>
          <input id="selectp1" type="text" autoComplete="on" list="p1"/> 
          <datalist id="p1">
              <option>First option</option>
              <option>Second Option</option>
          </datalist>
          <input id="selectp2" type="text" autoComplete="on" list="p2"/> 
          <datalist id="p2">
              <option>First option</option>
              <option>Second Option</option>
          </datalist>
          <button type="button" onClick={() => getplayernames(document.getElementById("selectp1").value,document.getElementById("selectp2").value)}>compare</button>
      </div>
      
  );
}

export default App;
