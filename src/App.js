import "./App.css"
import Header from "./components/common/heading/Header"
import { BrowserRouter as Router, Switch, Route } from "react-router-dom"
import Home from "./components/home/Home"
import About from "./components/about/About"
import CourseHome from "./components/allcourses/CourseHome"
import Contact from "./components/contact/Contact"
import AssignmentsHome from "./components/assignments/AssignmentsHome"
import Footer from "./components/common/footer/Footer"
import Bulletin from "./components/bulletin/Bulletin"

const App = () => {

  return (
    <>
      <Router>
        <Header />
        <Switch>
        <Route exact path='/' component={Home} />
        <Route exact path='/about' component={About} />
        <Route exact path='/courses' component={CourseHome} />
        <Route exact path='/contact' component={Contact} />
        <Route exact path='/assignments' component={AssignmentsHome} />
        <Route exact path='/bulletin' component={Bulletin} />
        </Switch>
        <Footer />
      </Router>
    </>
  )
}

export default App
