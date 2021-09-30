import logo from './logo.png';
import './App.css';
import React, { Component } from 'react';
import Project from "../projects/"


class Bottlescomp extends React.Component {
  constructor(props) {
    super(props);
    this.state = {text: "99 Bottles", bottles: 99, bottling: false, timer: "", button_a: "Next", button_b: "Play"};
    this.dobottles = this.dobottles.bind(this);
  }
  componentDidUpdate() {
    this.scrollToBottom();
  }
  scrollToBottom() {
    this.el.scrollIntoView({ behavior: 'smooth' });
  }
  jsbottles(bottles) {
    if (bottles > 0){
        bottles = bottles - 1;
        return `
${bottles+1} bottles of beer on the wall,
${bottles+1} bottles of beer.
Take one down, pass it around.
${bottles} bottles of beer on the wall.`;
    }
    }
  dobottles() {
    if(this.state.text === undefined) {return}
    else {
    if (this.state.bottles>0) {
        this.setState({ text: this.state.text + "\n" + this.jsbottles(this.state.bottles), bottles: this.state.bottles - 1, bottling: this.state.bottling});
      }
    };
  }
  render() {
    return (
    <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <h1>
             99 Bottles
        </h1>
        <div>
        <br />
        <span style={{ whiteSpace: 'pre' }}>
            {this.state.text}
        </span>
        </div>
        <br />
        <div>
        <button class="appbutton" onClick={this.dobottles}>
          {this.state.button_a} {this.state.bottles}
        </button>
        <button class="appbutton" onClick={() => {if (this.state.bottling === false) {
let t = setInterval(this.dobottles, 2000);
this.setState({bottling: true, button_b: "Pause", timer: t})
} else
{clearInterval(this.state.timer); 
this.setState({bottling: false, timer: "", button_a: "Next", button_b: "Play"})}}}>
        {this.state.button_b}
        </button>
        </div>
        <div ref={el => { this.el = el; }} />
        <button class="appbutton" onClick={() => {clearInterval(this.state.timer); this.setState({bottles: 99, text: "99 Bottles", bottling: false, timer: "", button_a: "Next", button_b: "Play"})}}> Reset </button>
      <Project />
      </header>
    );
  }
}

export default Bottlescomp;
