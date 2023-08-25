@app.route('/tags/<tag_name>/')
def tag(tag_name):
    tag = Tag.query.filter_by(name=tag_name).first_or_404()
    return render_template('tag.html', tag=tag)
