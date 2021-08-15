import React, { createContext } from 'react';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
//Pages
import Search from './pages/Search';
import Recommend from './pages/Recommend';
import Landing from './pages/Landing';

export const GlobalContext = createContext();

const App = () => {
	return (
		<GlobalContext.Provider>
			<Router>
				<Switch>
					<Route exact path="/" component={Landing} />
					<Route exact path="/search" component={Search} />
					<Route exact path="/recommend" component={Recommend} />
				</Switch>
			</Router>
		</GlobalContext.Provider>
	);
};

export default App;
