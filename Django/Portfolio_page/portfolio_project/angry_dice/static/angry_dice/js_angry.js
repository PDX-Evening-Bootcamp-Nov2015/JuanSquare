// Angry dice
/*
List of components:
  Die object constructor
  Game object
    Lots of data
    hold Function
    roll Function
    evaluate Function
    Populate HTML roll space function
    reset game function
*/

// Die object constructor
function Die() {
  this.held = false;
  this.val = 1;
  // change the value if die is not held
  this.roll = function () {
    if (this.held) {
      return;
    }
    this.val = Math.floor(Math.random() * 6) + 1;
  };
}

// Game object constructor
function Game(){
  // stage will be 1, 2, or 3
  this.stage = 1;
  // dice will be an array of two die objects
  this.dice = [];
  this.dice[0] = new Die();
  this.dice[1] = new Die();
  // table defining valid holds for each stage
  this.validHolds = {
    1 : [1, 2],
    2 : [3, 4],
    3 : [5]
  };
  // table defining pass conditions for each stage
  this.winStates = {
    1 : [1, 2],
    2 : [3, 4],
    3 : [5, 6]
  };

  // function to determine which die was clicked and hold
  this.clickHold = function () {
    var clickedImg = event.target,
        dieIndex = parseInt(clickedImg.id.charAt(3)),
        clickedDie = this.dice[dieIndex].val,
        validStageHolds = this.validHolds[this.stage];
    // check to make sure an image is clicked, exit if container was clicked
    // instead of image
    if (clickedImg.id === 'dice_area') {
      return;
    }
    // check to make sure the die has a value that can be held in this stage
    if (clickedDie === validStageHolds[0]
    || clickedDie === validStageHolds[1]) {
      this.dice[dieIndex].held = true;
      clickedImg.classList.add('held');
    }
  };

  // function to reset hold state of both dice
  this.resetHold = function () {
    this.dice[0].held = false;
    this.dice[1].held = false;
  };

  // you win Function
  this.youWin = function() {
    var stageNum = document.getElementById('stage_num'),
        rollButton = document.getElementById('roll');
    alert('You win!');
    stageNum.innerText = 'You win!';
    rollButton.value = 'Play Again!';
    this.stage = 4;
  };

  // reset roll button value after game win
  this.newGameReset = function() {
    var rollButton = document.getElementById('roll'),
        diceArea = document.getElementById('dice_area');
    diceArea.innerHTML = '';
    this.stage = 1;
    this.updateStage();
    rollButton.value = 'Roll!';
  };

  // function to evaluate the state of the game object
  this.evalState = function () {
    var diceArray = [this.dice[0].val, this.dice[1].val],
        winState = this.winStates[this.stage];
    // if 2 angry dice
    if (diceArray[0] === 3 && diceArray[1] === 3) {
      // reset to stage 1
      this.stage = 1;
      // reset held condition
      this.resetHold();
      // empty dice area
    } else if (!(diceArray.indexOf(winState[0]) === -1) &&
               !(diceArray.indexOf(winState[1]) === -1)) {
    // else if passing conditions
      // if stage 3
      if (this.stage === 3) {
        // win!
        this.youWin();
      } else {
        // advance stage
        this.stage += 1;
        // reset held condition
        this.resetHold();
      }
    }
  };
  // Function to populate HTML
  this.printDice = function () {
    // this function takes the entire game object as a parameter
    var diceArea = document.getElementById('dice_area'),
        // variable below contains the dice array from the game object
        dice = this.dice,
        i;
    // clear diceArea of previous round values
    diceArea.innerHTML = '';
    // use a loop to add new img elements for each die element
      // use of a loop here allows function to be scaled more easily later
    for (i = 0; i < this.dice.length; i++) {
      var newImg = document.createElement('img'),
          // retreive last roll value for die
          dieVal = dice[i].val,
          // retreive whether die is held
          held = dice[i].held;
      // show this is a die
      newImg.classList.add('die');
      // select correct image
      newImg.src = dieVal + '.png';
      // which die are we talking about?!
      newImg.id = 'die' + (i);
      if (held) {
        // add the held class for special formatting if die is held
        newImg.classList.add('held');
      }
      // throw it all into the document
      diceArea.appendChild(newImg);
    }
  };

  // update the stage on the html page
  this.updateStage = function(){
    var stageHolder = document.getElementById('stage_num');
    stageHolder.innerText = this.stage;
  };

  // function to roll both dice in the dice array
  this.roll = function () {
    // check to see if the user is starting a new game
    if (this.stage === 4) {
      this.resetHold();
      this.newGameReset();
      // reset the game and exit without rolling
      return;
    }
    // roll them dice
    this.dice[0].roll();
    this.dice[1].roll();
    // check game state and advance
    this.evalState();
    // display the dice state
    this.printDice();
    // display the stage state
    this.updateStage();
  };

  // function to parse key presses and perform appropriate action
  this.parseKey = function(){
    var key = event.keyCode;
    // if spacebar roll the dice
    if (key === 32) {
      this.roll();
    }
  };
}

window.onload = function(){
  var // initialize the game object
      theGame = new Game();
      // cache the roll button
      rollButton = document.getElementById('roll'),
      diceArea = document.getElementById('dice_area');
  // Add event listeners
    // roll click event
  rollButton.addEventListener('click', function(){
    theGame.roll();
  }, false);
  window.addEventListener('keydown', function(){
    theGame.parseKey();
  }, false)
  diceArea.addEventListener('click', function(){
    theGame.clickHold();
  }, false)
};
