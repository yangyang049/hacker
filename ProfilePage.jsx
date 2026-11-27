export default function ProfilePage({ user }) {
  return (
    <div className="profile-card">
      <h2>{user.name}</h2>
      <p className="user-email">이메일: {user.email.toLowerCase()}</p>
      <p>가입일: {user.created_at}</p>
    </div>
  );
}
