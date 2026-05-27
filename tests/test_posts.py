import pytest


class TestPosts:
    def test_get_posts_list(self, api_session, base_url):
        response = api_session.get(f"{base_url}/posts")

        assert response.status_code == 200

        posts = response.json()

        assert isinstance(posts, list)
        assert len(posts) > 0

    @pytest.mark.parametrize("post_id", [1, 2, 3])
    def test_get_post_by_id(self, api_session, base_url, post_id):
        response = api_session.get(f"{base_url}/posts/{post_id}")

        assert response.status_code == 200

        post = response.json()

        assert post["id"] == post_id
        assert "userId" in post
        assert "title" in post
        assert "body" in post

    def test_get_not_found_post(self, api_session, base_url):
        response = api_session.get(f"{base_url}/posts/857367865")

        assert response.status_code == 404
        assert response.json() == {}

    def test_create_post(self, api_session, base_url):
        new_post = {
            "title": "Test title",
            "body": "Test body",
            "userId": 1,
        }

        response = api_session.post(f"{base_url}/posts", json=new_post)

        assert response.status_code == 201

        created_post = response.json()

        assert created_post["title"] == new_post["title"]
        assert created_post["body"] == new_post["body"]
        assert created_post["userId"] == new_post["userId"]
        assert "id" in created_post

    def test_update_post(self, api_session, base_url):
        updated_post = {
            "id": 1,
            "title": "Updated title",
            "body": "Updated body",
            "userId": 1,
        }

        response = api_session.put(f"{base_url}/posts/1", json=updated_post)

        assert response.status_code == 200

        post = response.json()

        assert post["id"] == updated_post["id"]
        assert post["title"] == updated_post["title"]
        assert post["body"] == updated_post["body"]
        assert post["userId"] == updated_post["userId"]

    def test_delete_post(self, api_session, base_url):
        response = api_session.delete(f"{base_url}/posts/1")

        assert response.status_code == 200