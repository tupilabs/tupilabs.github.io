---
title: Blog
time: '17:10:48'
format: html
posts_filters:
    has_tags: blog
    not:
        is_draft: true
---

<div class="ui basic segment" id="blog">
    <div class="ui stackable grid container">
        <div class="row">
            <div class="sixteen wide column">
                <h1>Blog</h1>
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
                <section>
                    {% if pagination.prev_page %}<div class="prev"><a href="{{ pagination.prev_page }}">Next Posts</a></div>{% endif %}
                    {% if pagination.next_page %}<div class="next"><a href="{{ pagination.next_page }}">Previous Posts</a></div>{% endif %}
                </section>
                {% endif %}
            </div>
        </div>
    </div>
</div>

