from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from rest_framework.validators import UniqueTogetherValidator


from posts.models import Comment, Post, Follow, Comment, Group, User


class ApiPostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(
        slug_field='username',
        read_only=True,
    )

    class Meta:
        fields = '__all__'
        model = Post


class ApiCommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        default=serializers.CurrentUserDefault(),
        read_only=True,
        slug_field='username',
    )
    post = serializers.PrimaryKeyRelatedField(
        read_only=True,
    )

    class Meta:
        fields = '__all__'
        model = Comment


class ApiFollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        default=serializers.CurrentUserDefault(),
        slug_field='username',
        read_only=True,
    )
    following = serializers.SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all()
    )

    def validate_following(self, following):
        if self.context.get('request').method != 'POST':
            return following
        if self.context['request'].user == following:
            raise serializers.ValidationError('Cant be subscribed on yourself')
        return following

    class Meta:
        fields = '__all__'
        model = Follow
        read_only_fields = ('user', 'following')

        validators = [
            UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=('user', 'following')
            )
        ]


class ApiGroupSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Group
