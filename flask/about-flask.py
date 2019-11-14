import flask
import flask_bootstrap
import flask_wtf
import flask_mail
import wtforms


class nameform(flask_wtf.FlaskForm):  # 定义表单类（newindex中用到）
    name = wtforms.StringField('input your name', validators=[wtforms.validators.DataRequired()])
    submit = wtforms.SubmitField('提交')


app = flask.Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'  # 密钥
bootstrap = flask_bootstrap.Bootstrap(app)


@app.route('/')
def index():
    another = 'blablabla'
    li = [1, 2, 3, 4, 5]
    dict1 = {'name': "ronnie", 'age': 22}
    return flask.render_template('user.html', text=another, li=li, dict1=dict1)
    # 通过传递关键词参数将another的值传到.html中，在.html文件中以{{text表示}}


@app.route('/new', methods=['GET', 'POST'])
def newindex():  # 连接到模板页面
    form = nameform()
    if form.validate_on_submit():
        flask.session['name'] = form.name.data  # 使用字典储存
        if flask.session.get('name').isdigit():
            flask.flash('is digit!go to old index!')  # 要在.html中也设置好才能显示
            return flask.render_template('newhome.html', form=form, name=flask.session.get('name'))
        form.name.data = ''
    return flask.render_template('newhome.html', form=form, name=flask.session.get('name'))
# name通过字典查询的方式传入值


@app.route('/user/<username>')
def name(aname):
    return '<h1>hello {}<h1>'.format(aname)


@app.route('/id/<userid>')
def userid(userid):
    if int(userid) > 100:
        flask.abort(404)
    else:
        return '<h1>hello {}<h1>'.format(userid)


if __name__ == '__main__':
    app.run(debug=True)
