import logo from './logo.svg';
import './App.css';
import DialogBox from './mod/Dialog';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <DialogBox/>
      </header>
    </div>
  );
}

export default App;
