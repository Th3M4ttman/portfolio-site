class _icons {
  constructor (props) {
    this.flask = "./icons/frameworks/flask.svg";
    this.nodejs = "./icons/frameworks/nodejs.svg";
    this.qt = "./icons/frameworks/qt.svg";
    this.react = "./icons/frameworks/react.svg";
    this.sqlalchemy = "./icons/frameworks/sqlalchemy.svg";

    this.frameworks = [
      this.nodejs,
      this.react,
      this.flask,
      this.qt,
      this.sqlalchemy
    ]

    this.bash = "./icons/languages/bash.svg";
    this.cpp = "./icons/languages/cplusplus.svg";
    this.js = "./icons/languages/javascript.svg";
    this.kotlin = "./icons/languages/kotlin.svg";
    this.php = "./icons/languages/php.svg";
    this.python = "./icons/languages/python.svg";
    this.r = "./icons/languages/r.svg";
    this.ts = "./icons/languages/typescript.svg";

    this.languages = [
      this.js,
      this.ts,
      this.cpp,
      this.python,
      this.r,
      this.kotlin,
      this.bash,
      this.php
    ]

    this.ae = "./icons/software/aftereffects.svg";
    this.gimp = "./icons/software/gimp.svg";
    this.ps = "./icons/software/photoshop.svg";
    this.pycharm = "./icons/software/pycharm.svg";
    this.unity = "./icons/software/unity.svg";
    this.unreal = "./icons/software/unreal.svg";
    this.vscode = "./icons/software/vscode.svg";
    this.mysql = "./icons/languages/mysql.svg";


    this.software = [
      this.mysql,
      this.ae,
      this.ps,
      this.gimp,
      this.vscode,
      this.pycharm,
      this.unreal,
      this.unity
    ]

    this.git = "./icons/versioning/git.svg";
    this.github = "./icons/versioning/github.svg";

    this.versioning = [
      this.git,
      this.github
    ]

    this.bootsrap = "./icons/web/bootstrap.svg";
    this.css = "./icons/web/css3.svg";
    this.heroku = "./icons/web/heroku.svg";
    this.html = "./icons/web/html5.svg";
    this.ssh = "./icons/languages/ssh.svg";
    this.web = [
      this.html,
      this.css,
      this.bootsrap,
      this.heroku,
      this.ssh
    ]

  }
  img(icon, width = "50px", height = "50px", alt = "Icon") {
    return (
      <img src={icon} width={width} height={height} alt={alt} />
    )
  }
  imgs(category = null, width = "50px", height = "50px", alt = "Icon") {
    this.out = [];
    this.out.push(<h2> Proficiencies </h2>)
    if (category === null) {
      this.outl = []
      this.out.push(<h3> Languages </h3>)
      for (let i in icons.languages) {
        this.outl.push(
          <img src={icons.languages[i]} width={width} height={height} alt={alt} />
        )
      }
      this.out.push(<div className="icons">
 {this.outl}
      </div>
      )
      this.out.push(<h3> Software </h3>)
      this.outl = []
      for (let i in icons.software) {
        this.outl.push(
          <img src={icons.software[i]} width={width} height={height} alt={alt} />
        )
      }
      this.out.push(<div className="icons">
 {this.outl}
      </div>
      )
      this.out.push(<h3> Frameworks </h3>)
      this.outl = []
      for (let i in icons.frameworks) {
        this.outl.push(
          <img src={icons.frameworks[i]} width={width} height={height} alt={alt} />
        )
      }
      this.out.push(<div className="icons">
 {this.outl}
      </div>
      )
      this.out.push(<h3> Web </h3>)
      this.outl = []
      for (let i in icons.web) {
        this.outl.push(
          <img src={icons.web[i]} width={width} height={height} alt={alt} />
        )
      }
      this.out.push(<div className="icons">
 {this.outl}
      </div>
      )
      this.out.push(<h3> Versioning </h3>)
      this.outl = []
      for (let i in icons.versioning) {
        this.outl.push(
          <img src={icons.versioning[i]} width={width} height={height} alt={alt} />
        )
      }
      this.out.push(<div className="icons">
 {this.outl}
      </div>
      )
      console.log(this.out)
      return (this.out)
    }
  }
}

const icons = new _icons();

export default icons