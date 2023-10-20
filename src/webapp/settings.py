# We will place the endpoints here
from flask import Blueprint, render_template
from flask_login import login_required, current_user
from flask import request, redirect, url_for
from . import user_manager

settings = Blueprint('settings', __name__)


@settings.route('/background_selector', methods=['GET', 'POST'])
@login_required
def background_selector():
    if request.method == 'POST':
        preferred_background = request.form.get('selected_background')

        # Update background for the current user
        user_manager.update_preferred_background(current_user.username, preferred_background)

        return redirect(url_for('views.landing_page'))  # Redirect to the home page after saving

    return render_template('background_selector.html',
                           background_images=['background_image.jpg', 'background_image_2.png',
                                              'background_image_3.png', 'background_image_4.png',
                                              'background_image_5.png', 'background_image_6.png',
                                              'background_image_7.png', 'background_image_8.png'])
