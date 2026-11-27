export default function ProfilePage({ user }) {
  return (
    <div className="profile-card">
      <h2>{user.name}</h2>
      <p>가입일: {user.created_at}</p>
    </div>
  );
}
