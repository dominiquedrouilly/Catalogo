// Source: https://www.digitalocean.com/community/tutorials/how-to-add-login-authentication-to-react-applications

import React, { createContext, useState, useCallback, useMemo } from "react";

export const TokenContext = createContext();

export function TokenProvider({ children }) {
  const [token, setTokenState] = useState(() => {
    const tokenString = sessionStorage.getItem("token");
    return tokenString ?? null;
  });

  const setToken = useCallback((newToken) => {
    if (newToken) {
      sessionStorage.setItem("token", newToken);
    } else {
      sessionStorage.removeItem("token");
    }
    setTokenState(newToken);
  }, []);

  const contextValue = useMemo(
    () => ({
      token,
      setToken,
    }),
    [token, setToken]
  );

  return (
    <TokenContext.Provider value={contextValue}>
      {children}
    </TokenContext.Provider>
  );
}
