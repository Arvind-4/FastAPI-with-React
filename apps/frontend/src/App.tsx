import React from 'react';
import './app.scss';
import { Content, Theme } from '@carbon/react';
import TutorialHeader from './components/TutorialHeader';
import { Route, Switch } from 'react-router-dom';
import LandingPage from './content/LandingPage';
import RepoPage from './content/RepoPage';

import LoginPage from './content/LoginPage';
import RegisterPage from './content/RegisterPage';

function App() {
  return (
    <>
      <Theme theme="g100">
        <TutorialHeader />
      </Theme>
      <Content>
        <Switch>
          <Route exact path="/" component={LandingPage} />
          <Route exact path="/login" component={LoginPage} />
          <Route exact path="/register" component={RegisterPage} />
          <Route exact path="/repo" component={RepoPage} />
        </Switch>
      </Content>
    </>
  );
}

export default App;
