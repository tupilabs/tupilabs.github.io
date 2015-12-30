---
title: Tutorials
time: '19:06:21'
format: html
posts_filters:
    has_tags: tutorial
    not:
        is_draft: true
---

<div class="ui basic segment" id="tutorials">
    <div class="ui stackable grid container">
        <div class="row">
            <div class="sixteen wide column">
                <h1>Tutorials</h1>
            </div>
        </div>
        <div class="row">
            <div class="sixteen wide column">
                {% if pagination.has_posts %}
                <section>
                    {% for post in pagination.posts %}
                    {% include 'partial_post.html' %}
                    {% endfor %}
                </section>
                <hr class="ui divider" />
                <div class="ui pagination menu">
                    {% if pagination.next_page %}
                    <a class="item" href="{{ pagination.next_page }}"><i class='left arrow icon'></i> Previous Posts</a>
                    {% endif %}
                    {% if pagination.prev_page %}
                    <a class="item" href="{{ pagination.prev_page }}"><i class='right arrow icon'></i> Next Posts</a>
                    {% endif %}
                </div>
                {% endif %}
            </div>
        </div>
    </div>
</div>

